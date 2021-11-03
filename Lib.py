import cv2 as cv

class image:
    def __init__(self,template,fullscreen):
        self.template   = template
        self.fullscreen = fullscreen

    def search_image(self):
        # Input
        template   = cv.imread(self.template)
        fullscreen = cv.imread(self.fullscreen)
        threshold  = 0.01           # Default setting by Omnipollo
        # Output
        x1,y1,x2,y2 = 0,0,0,0       # UpperLeft(x1,y1) BottomRight(x2,y2)
        bkr = False                 # Breaker; if matching, True
        # Process
        h,w = template.shape[:2]    # Template size
        res = cv.matchTemplate(fullscreen, template, cv.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        if min_val < threshold:
            bkr = True
            x1,y1,x2,y2 = min_loc[0], min_loc[1], min_loc[0]+w, min_loc[1]+h
        return x1,y1,x2,y2,bkr
