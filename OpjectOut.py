import numpy as np
import sys
import cv2

class CvImage():
    def __init__(self) -> None:
        
        self.photo = np.zeros((300, 300, 3), dtype='uint8')
    
    def show(self) -> None:

        cv2.imshow('Photo', self.photo)
        cv2.waitKey(0)

    def change_bgr(self, blue: int = 255, green: int = 255, red: int = 255) -> None:
        # I use change for all elems of arr
                # from to format or None for all
        self.photo[100:150, 200:200] = blue, green, red # Or I can use sape 

        return None
    
    def figures_crt(self):

        return None
class main_build():
    def __init__(self) -> None:
        
        CvObj = CvImage()
        CvObj.show()

        return None

main_build() 