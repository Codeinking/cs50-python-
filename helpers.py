'''a file is just a sequence of bits, arranged in some fashion. A 24-bit BMp file is essenstially just a sequence of bits, (almost) every 24 of which represent some pixel color. BMP file also contains "metadata", information like an image's height and width, and this data is stored at the beginning of the file in form of two data structure generally referred to as "headers".1. BITMAPINFOHEADER: 40 bytes long,   BITMAPFILEHEADER: 14 BYTES long, following this two headers is the actual BITMAP: an array of bytes,triples which represent a pixel colour, BMP stores triples in reverse(BGR) with 8 bits for each, some also store the entire bitmap backwards, with an image top row at the end of BMP file'''


import math

from PIL import Image
import sys, os 
import struct



def filter(input):
    file_path = input

    # Check that the file exists
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        return

    # Open BMP file in binary mode
    with open(file_path, "rb") as image_in:

        # -------------------------------------------------
        # BITMAP FILE HEADER - 14 bytes
        # -------------------------------------------------

        file_header = image_in.read(14)

        if len(file_header) != 14:
            print(
                f"Error: Expected 14 bytes for BMP file header, "
                f"but got {len(file_header)}."
            )
            return

        # < = little-endian
        # 2s = signature (2 bytes)
        # I  = file size (4 bytes)
        # H  = reserved 1 (2 bytes)
        # H  = reserved 2 (2 bytes)
        # I  = pixel data offset (4 bytes)

        magic, file_size, reserved1, reserved2, pixel_offset = struct.unpack(
            "<2sIHHI",
            file_header
        )

        # Check BMP signature
        if magic != b"BM":
            print(f"Error: This is not a BMP file. Signature: {magic}")
            return

        print("========== BMP FILE HEADER ==========")
        print(f"Signature:      {magic.decode('ascii')}")
        print(f"File size:      {file_size} bytes")
        print(f"Reserved 1:     {reserved1}")
        print(f"Reserved 2:     {reserved2}")
        print(f"Pixel offset:   {pixel_offset} bytes")

        # -------------------------------------------------
        # DIB HEADER
        # -------------------------------------------------

        # First 4 bytes tell us the size of the DIB header
        dib_size_data = image_in.read(4)

        if len(dib_size_data) != 4:
            print("Error: Could not read DIB header size.")
            return

        dib_size = struct.unpack("<I", dib_size_data)[0]

        print("\n========== DIB HEADER ==========")
        print(f"DIB header size: {dib_size} bytes")

        # We need at least 40 bytes for BITMAPINFOHEADER
        if dib_size < 40:
            print(
                f"Error: Unsupported BMP DIB header size: {dib_size} bytes."
            )
            return

        # We already read 4 bytes of the DIB header.
        # Read the remaining 36 bytes of the standard 40-byte header.
        dib_rest = image_in.read(36)

        if len(dib_rest) != 36:
            print("Error: Incomplete DIB header.")
            return

        dib_header = dib_size_data + dib_rest

        # BITMAPINFOHEADER structure
        (
            header_size,
            width,
            height,
            planes,
            bits_per_pixel,
            compression,
            image_size,
            x_pixels_per_meter,
            y_pixels_per_meter,
            colors_used,
            important_colors
        ) = struct.unpack(
            "<IiiHHIIiiII",
            dib_header[:40]
        )

        # -------------------------------------------------
        # DISPLAY IMAGE INFORMATION
        # -------------------------------------------------

        print(f"Width:           {width} pixels")
        print(f"Height:          {height} pixels")
        print(f"Color planes:    {planes}")
        print(f"Bits per pixel:  {bits_per_pixel}")
        print(f"Compression:     {compression}")
        print(f"Image size:      {image_size} bytes")
        print(f"X resolution:    {x_pixels_per_meter} pixels/m")
        print(f"Y resolution:    {y_pixels_per_meter} pixels/m")
        print(f"Colors used:     {colors_used}")
        print(f"Important colors:{important_colors}")

        # -------------------------------------------------
        # BASIC VALIDATION
        # -------------------------------------------------

        print("\n========== VALIDATION ==========")

        if planes != 1:
            print("Warning: BMP should normally have 1 color plane.")
        else:
            print("Color planes: OK")

        supported_bpp = [1, 4, 8, 16, 24, 32]
        if bits_per_pixel not in supported_bpp:
            print(
                f"Warning: {bits_per_pixel}-bit BMP may not be supported."
            )
        else:
            print(f"Bit depth: {bits_per_pixel}-bit")

        # Compression 0 means BI_RGB (uncompressed)
        if compression == 0:
            print("Compression: Uncompressed (BI_RGB)")
        else:
            print(f"Compression type: {compression}")

        # -------------------------------------------------
        # FILE SIZE CHECK
        # -------------------------------------------------

        actual_file_size = os.path.getsize(file_path)

        print(f"\nActual file size: {actual_file_size} bytes")

        if actual_file_size == file_size:
            print("File size check: OK")
        else:
            print(
                "Warning: Header file size does not match "
                "the actual file size."
            )

        # -------------------------------------------------
        # PIXEL DATA LOCATION
        # -------------------------------------------------

        print(f"\nPixel data begins at byte: {pixel_offset}")

        # -------------------------------------------------
        # SUMMARY
        # -------------------------------------------------

        print("\n========== BMP SUMMARY ==========")
        print(f"File:       {file_path}")
        print(f"Dimensions: {width} x {abs(height)} pixels")
        print(f"Bit depth:  {bits_per_pixel}-bit")

        if height > 0:
            print("Orientation: Bottom-up")
        else:
            print("Orientation: Top-down")

        print("=================================")
        




def greyscale(input,output):
    with Image.open(input) as old_img:
        old_img = old_img.convert("RGB")
        width , height = old_img.size
        
        
        new_img = Image.new("RGB",(width,height))
        
        old_pixels = old_img.load()
        new_pixels = new_img.load()
        
        for y in range(height):
            for x in range(width):
                r,g,b = old_img.getpixel((x,y))
                            
                pixel_avg = (r + g + b) // 3
                                
                new_r = pixel_avg
                new_g = pixel_avg
                new_b =pixel_avg
                                
                new_pixels[x,y]= (new_r, new_g, new_b)
                
        new_img.save(output)
        
        
        
def serpia(input, output):
    
    with Image.open(input) as old_img:
            old_img = old_img.convert("RGB")
            width , height = old_img.size
            
            
            new_img = Image.new("RGB",(width,height))
            
            old_pixels = old_img.load()
            new_pixels = new_img.load()
            
            for y in range(height):
                for x in range(width):
                    r,g,b = old_img.getpixel((x,y))
                                
                   
                                    
                    new_r = int(.393 * r + .769 * g + .189 * b) % 255
                    new_g = int( .349 * r + .686 * g + .168 * b) % 255
                    new_b = int(.534 * r + .534 * g + .131 * b) % 255
                                    
                    new_pixels[x,y]= (new_r, new_g, new_b)
                    
            new_img.save(output)
 
def reflect(input,output):
    with Image.open(input) as old_img:
        old_img = old_img.convert("RGB")
        width , height = old_img.size
                 
                 
        new_img = Image.new("RGB",(width,height))
                 
        old_pixels = old_img.load()
        new_pixels = new_img.load()
                 
        for y in reversed(range(height)):
            for x in reversed(range(width)):
                r,g,b = old_img.getpixel((-x,y))
                         
                new_r = r
                new_g = g
                new_b = b
                         
    
                new_pixels[x,y] = (new_r,new_g ,new_b)

        new_img.save(output)        

def blur(input, output):
     with Image.open(input) as old_img:
            old_img = old_img.convert("RGB")
            width , height = old_img.size
                     
                     
            new_img = Image.new("RGB",(width,height))
                     
            old_pixels = old_img.load()
            new_pixels = new_img.load()
                     
            for y in range(height):
                for x in range(width):
                    if y == 0 and x == 0:
                        r_l,g_l,b_l = old_img.getpixel((x,y))
                        r_m,g_m,b_m = old_img.getpixel(((x+1),y)) 
                        r_p,g_p,b_p = old_img.getpixel((x+1,y+1))
                        r_o,g_o,b_o = old_img.getpixel((x,y+1))
                
                             
                        new_r = (r_l + r_m + r_p + r_o)//4
                        new_g = (g_l + g_m + g_p + g_o)//4
                        new_b = (b_l + b_m + b_p + b_o)//4
                            
                        new_pixels[x,y] = (new_r,new_g ,new_b)
                        
                    elif y == height-1  and x == 0:
                        r_l,g_l,b_l = old_img.getpixel((x,y))
                        r_m,g_m,b_m = old_img.getpixel((x+1,y)) 
                        r_i,g_i,b_i = old_img.getpixel((x,y-1))
                        r_j,g_j,b_j = old_img.getpixel((x+1,y-1))
                                        
                                                     
                        new_r = (r_l + r_m + r_i + r_j)//4
                        new_g = (g_l + g_m + g_i + g_j)//4
                        new_b = (b_l + b_m + b_i + b_j)//4
                            
                        new_pixels[x,y] = (new_r,new_g ,new_b)
                            
                    elif y == height-1   and x == width-1:
                        r_l,g_l,b_l = old_img.getpixel((x,y))
                        r_k,g_k,b_k = old_img.getpixel((x-1,y)) 
                        r_i,g_i,b_i = old_img.getpixel((x,y-1))
                        r_h,g_h,b_h = old_img.getpixel((x-1,y-1))
                                                                
                                                                             
                        new_r = (r_l + r_k + r_i + r_h)//4
                        new_g = (g_l + g_k + g_i + g_h)//4
                        new_b = (b_l + b_k + b_i + b_h)//4
                            
                        new_pixels[x,y] = (new_r,new_g ,new_b)
                            
                    elif y == 0  and x == width-1:
                        r_l,g_l,b_l = old_img.getpixel((x,y))
                        r_o,g_o,b_o = old_img.getpixel((x,y+1)) 
                        r_n,g_n,b_n = old_img.getpixel((x-1,y+1))
                        r_k,g_k,b_k = old_img.getpixel((x-1,y))
                                                                
                                                                             
                        new_r = (r_l + r_o + r_n + r_k)//4
                        new_g = (g_l + g_o + g_n + g_k)//4
                        new_b = (b_l + b_o + b_n + b_k)//4 
                            
                        new_pixels[x,y] = (new_r,new_g ,new_b)
                            
                    elif y == height-1  and (0 < x < width-1):
                           r_l,g_l,b_l = old_img.getpixel((x,y))
                           r_k,g_k,b_k = old_img.getpixel((x-1,y))    
                           r_m,g_m,b_m = old_img.getpixel((x+1,y))
                           r_i,g_i,b_i = old_img.getpixel((x,y-1))
                           r_h,g_h,b_h = old_img.getpixel((x-1,y-1))
                           r_j,g_j,b_j = old_img.getpixel((x+1,y-1))

                            
                           new_r = (r_l + r_k + r_m  + r_i + r_h + r_j )//6
                           new_g = (g_l + g_k  + g_m + g_i + g_h + g_j )//6
                           new_b = (b_l + b_k  + b_m + b_i + b_h + b_j )//6
                        
                           new_pixels[x,y] = (new_r,new_g ,new_b)
                            
                    elif y == 0  and (0 < x < width-1):
                            
                            r_l,g_l,b_l = old_img.getpixel((x,y))
                            r_k,g_k,b_k = old_img.getpixel((x-1,y))    
                            r_m,g_m,b_m = old_img.getpixel((x+1,y))
                            r_o,g_o,b_o = old_img.getpixel((x,y-1))
                            r_n,g_n,b_n = old_img.getpixel((x-1,y+1))
                            r_p,g_p,b_p = old_img.getpixel((x+1,y+1))
                        
                                                    
                            new_r = (r_l + r_k + r_m + r_o + r_n + r_p)//6
                            new_g = (g_l + g_k + g_m + g_o + g_n + g_p)//6
                            new_b = (b_l + b_k + b_m + b_o + b_n + b_p)//6

                            new_pixels[x,y] = (new_r,new_g ,new_b)
                            
                    else:
                        
                        if x == 0:
                            r_l,g_l,b_l = old_img.getpixel((x,y))
                            r_i,g_i,b_i = old_img.getpixel((x,y-1))
                            r_o,g_o,b_o = old_img.getpixel((x,y+1))
                            r_j,g_j,b_j = old_img.getpixel((x+1,y-1))
                            r_m,g_m,b_m = old_img.getpixel((x+1,y))
                            r_p,g_p,b_p = old_img.getpixel((x+1,y+1))

                            new_r =  (r_l + r_i + r_o + r_j + r_m + r_p)//6 
                            new_g = (g_l + g_i + g_o + g_j + g_m + g_p)//6
                            new_b =  (b_l + b_i + b_o + b_j + b_m + b_p)//6
                            
                        elif x == width-1:
                        
                            r_l,g_l,b_l = old_img.getpixel((x,y))
                            r_i,g_i,b_i = old_img.getpixel((x,y-1))
                            r_o,g_o,b_o = old_img.getpixel((x,y+1))
                            r_j,g_j,b_j = old_img.getpixel((x-1,y-1))
                            r_m,g_m,b_m = old_img.getpixel((x-1,y))
                            r_p,g_p,b_p = old_img.getpixel((x-1,y+1))
                        
                            new_r =  (r_l + r_i + r_o + r_j + r_m + r_p)//6 
                            new_g = (g_l + g_i + g_o + g_j + g_m + g_p)//6
                            new_b =  (b_l + b_i + b_o + b_j + b_m + b_p)//6
                           
                        else:    
                            r_l,g_l,b_l = old_img.getpixel((x,y))
                            r_k,g_k,b_k = old_img.getpixel((x-1,y))  
                            r_m,g_m,b_m = old_img.getpixel((x+1,y))
                            r_o,g_o,b_o = old_img.getpixel((x,y-1))
                            r_n,g_n,b_n = old_img.getpixel((x-1,y+1))
                            r_p,g_p,b_p = old_img.getpixel((x+1,y+1))
                            r_i,g_i,b_i = old_img.getpixel((x,y-1))
                            r_h,g_h,b_h = old_img.getpixel((x-1,y-1))
                            r_j,g_j,b_j = old_img.getpixel((x+1,y-1))
                        
                            new_r = (r_l + r_k + r_m + r_o + r_n + r_p + r_i + r_h + r_j)//9
                            new_g = (g_l + g_k + g_m + g_o + g_n + g_p + g_i + g_h + g_j ) //9
                            new_b = (b_l + b_k + b_m + b_o + b_n + b_p + b_i + b_h + b_j  )//9                            


                            new_pixels[x,y] = (new_r,new_g ,new_b)
            
            new_img.save(output)      

def edge(input, output):
     with Image.open(input) as old_img:
            old_img = old_img.convert("RGB")
            width , height = old_img.size
                     
                     
            new_img = Image.new("RGB",(width,height))
                     
            old_pixels = old_img.load()
            new_pixels = new_img.load()
                     
            for y in range(height):
                for x in range(width):
                    if y == 0 or y == height-1 or x == 0 or x == width-1:
                        r,g,b = old_img.getpixel((x,y))
                                                 
                        new_r = 0
                        new_g = 0
                        new_b = 0
                                                 
                            
                        new_pixels[x,y] = (new_r,new_g ,new_b)
                        
                    else:
                        
                        
                        r_l,g_l,b_l = old_img.getpixel((x,y))
                        r_k,g_k,b_k = old_img.getpixel((x-1,y))  
                        r_m,g_m,b_m = old_img.getpixel((x+1,y))
                        r_o,g_o,b_o = old_img.getpixel((x,y+1))
                        r_n,g_n,b_n = old_img.getpixel((x-1,y+1))
                        r_p,g_p,b_p = old_img.getpixel((x+1,y+1))
                        r_i,g_i,b_i = old_img.getpixel((x,y-1))
                        r_h,g_h,b_h = old_img.getpixel((x-1,y-1))
                        r_j,g_j,b_j = old_img.getpixel((x+1,y-1))
                        
                                               
                        gx_r = ((r_l * 0) + (r_k *(-2)) + (r_m * 2) + (r_o * 0) + (r_n * (-1)) + (r_p * 1) + (r_i * 0) + (r_h * (-1)) + (r_j * 1))
                        gx_g = ((g_l * 0) + (g_k *(-2)) + (g_m * 2) + (g_o * 0) + (g_n * (-1)) + (g_p * 1) + (g_i * 0) + (g_h * (-1)) + (g_j * 1))
                        gx_b = ((b_l * 0) + (b_k *(-2)) + (b_m * 2) + (b_o * 0) + (b_n * (-1)) + (b_p * 1) + (b_i * 0) + (b_h * (-1)) + (b_j * 1))                            
                       
                        gy_r = ((r_l * 0) + (r_k * 0) + (r_m * 0) + (r_o * 2) + (r_n * 1) + (r_p * 1) + (r_i *(-2)) + (r_h *(-1)) + (r_j * (-1)))
                        gy_g = ((g_l * 0) + (g_k * 0) + (g_m * 0) + (g_o * 2) + (g_n * 1) + (g_p * 1) + (g_i *(-2)) + (g_h *(-1)) + (g_j * (-1)))
                        gy_b = ((b_l * 0) + (b_k * 0) + (b_m * 0) + (b_o * 2) + (b_n * 1) + (b_p * 1) + (b_i *(-2)) + (b_h *(-1)) + (b_j * (-1)))   
                       
                        new_r = min(255, round(math.sqrt((gx_r ** 2) + (gy_r ** 2))))
                        new_g = min(255, round(math.sqrt((gx_g ** 2) + (gy_g ** 2))))
                        new_b = min(255, round(math.sqrt((gx_b ** 2) + (gy_b ** 2))))
                        
                        new_pixels[x,y] = (new_r,new_g ,new_b)
                        
            new_img.save(output)     
   
# ---------------------------------------------------------
# COMMAND-LINE FUNCTION DISPATCHER
# ---------------------------------------------------------

if __name__ == "__main__":

    functions = {
        "filter": filter,
        "s"     : serpia,
        "g"     : greyscale,
        "r"     : reflect,
        "b"     : blur,
        "e"     : edge,

    }

    if len(sys.argv) < 2:
        print("Usage:")
        print("    python helpers.py filter")
        sys.exit(1)

    requested_function = sys.argv[1]
   
    

    if requested_function in functions and len(sys.argv) == 3:
        input = sys.argv[2]
        functions[requested_function](input)
    elif requested_function in functions and len(sys.argv) == 4:
        input = sys.argv[2]
        output = sys.argv[3]
        functions[requested_function](input,output)
    else:
        print(f"Unknown function: {requested_function}")
        print("Available functions:")
        for function_name in functions:
            print(f"    {function_name}")


'''this took a long time because firstly, i didnt even understand what was not required of me and what was. i used a lot of browsing and ai to get the filter function which was not required of me to work, also it is always important to put check and error messages in your code cause if i did in this at the earlier stage i would have been able to know that the image i wanted to use was not a good one, the rest of the function were relatively easier except the last, came up with the logic and i still had the idea on how to fix the problem but ended up using ai to fix the code. had to learn how to call function from the command line that did not match the name of the file and would be using this going forward , all in all i think this was the one project have spent so much time on, hopefully i get to finish the whole problem set and move on the next. but it had a lot of lessons and maybe later i would label the rest of the code'''

'''with the edge function it was relatively easy as i understood how the algorithm was to function, i did however not comprehend the steps properly, but however fixing the code to perform the right effect that was required was just a few steps from what was firstly produced, long story short Comprehension is key and for now i use Ai as the corrector of my code for now as i continue to get better and learn more syntax'''