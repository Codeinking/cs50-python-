import math

from PIL import Image



def greyscale():
    with Image.open("./images/convertico-coffee-bean-24-bit-bmp.bmp") as old_img:
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
                
        new_img.save("./images/new_image_2_greyscale.bmp")
        
        
        
def serpia():
    
    with Image.open("./images/convertico-coffee-bean-24-bit-bmp.bmp") as old_img:
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
                    
            new_img.save("./images/new_image_2_serpia.bmp")
 
def reflect():
    with Image.open("./images/convertico-coffee-bean-24-bit-bmp.bmp") as old_img:
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

        new_img.save("./images/new_image_2.bmp")        

def blur():
     with Image.open("./images/messi.jpeg") as old_img:
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
                            r_o,g_o,b_o = old_img.getpixel((x,y+1))
                            r_n,g_n,b_n = old_img.getpixel((x-1,y+1))
                            r_p,g_p,b_p = old_img.getpixel((x+1,y+1))
                            r_i,g_i,b_i = old_img.getpixel((x,y-1))
                            r_h,g_h,b_h = old_img.getpixel((x-1,y-1))
                            r_j,g_j,b_j = old_img.getpixel((x+1,y-1))
                        
                            new_r = (r_l + r_k + r_m + r_o + r_n + r_p + r_i + r_h + r_j)//9
                            new_g = (g_l + g_k + g_m + g_o + g_n + g_p + g_i + g_h + g_j ) //9
                            new_b = (b_l + b_k + b_m + b_o + b_n + b_p + b_i + b_h + b_j  )//9                            


                            new_pixels[x,y] = (new_r,new_g ,new_b)
            
            new_img.save("./images/new_image_2_blur.bmp")      
            
def edge():
     with Image.open("./images/new_image_2_greyscale.bmp") as old_img:
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
                        
            new_img.save("./images/new_image_3.bmp")        
                        

#serpia()
greyscale()    
#reflect()     
#blur()
edge()   