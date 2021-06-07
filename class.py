class Statue(object):
    def __init__(self, name, height, width, appearance, texture):
        self.name = name
        self.height = height
        self.width = width
        self.appearance = appearance
        self.texture = texture
    
    def walk(self):
        print(self.name + "is walking")

    def role(self):
        print(self.name + "has the role to guide the player")

    def changeTexture(self,Texture):
        self.texture = Texture
        print("Texture has changed")

statue1 = Statue("OldMan ",2,0.9,"messy","simpleMan")
statue1.walk()

statue2 = Statue("Major Stryker ",2.5,1,"serious","ArmySoldier")
statue2.role()
