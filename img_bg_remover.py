from withoutbg import WithoutBG

def remove_background(path,output_img_name):
    img = WithoutBG.opensource()
    try:
        result = img.remove_background(path)
        result.save(output_img_name)
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

output_img_name = input("Enter the name of the output image (with extension): ")
input_img_path = input("Enter the path of the input image: ")
result = remove_background(input_img_path, output_img_name)
if result:  
    print(f"Background removed successfully. Output saved as {output_img_name}")
else:    
    print("Failed to remove background.")