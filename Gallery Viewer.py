# Aap ke paas do lists hain:
# allImages → Saare images in order (like gallery)
# [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10]
# markedFavorites → Kuch selected images from above list (favorites)
# [i2, i5, i7]
# Ab aapko ek function banana hai:
# get_next()
# Har baar jab aap get_next() call karo, to:
# Pehle aapko markedFavorites ke images dene hain same order mein
# Uske baad allImages ke baaki images dene hain, jo markedFavorites mein nahi hain, original order mein.
# Aur jab sab images return ho chuke ho, tab None return karna hai.
# time Complexity : 0(N + M)
# Space Complexity : 0(N + M)
# self.markedFavorites store karta hai favorites as a set: O(N)
# self.allImages store karta hai all images as a set: O(M)

class Galary:
    def __init__(self, allImages, markedFavorites) :
        self.ordered = []
        self.markedFavorites = set(markedFavorites)
        self.allImages = allImages

        for image in markedFavorites: # 0(N) n is the number of favorates
            self.ordered.append(image)
        
        for image in allImages: # 0(M) m is the number of allImages
            if image not in markedFavorites:
                self.ordered.append(image)
        
        self.index = 0
    
    def get_next(self):
        if self.index >= len(self.ordered):
            return None

        image = self.ordered[self.index] #0(1)
        self.index += 1

        return image


gallary = Galary([11,12,13,14,15,16,17,18,19,10],[12,15,17])


item = gallary.get_next()
while item is not None:
    print(item)
    item = gallary.get_next()
