# Advanced Rule-Based Image Captioning

def generate_caption(image_name):
    name = image_name.lower()

    objects = []
    actions = []

    # Object detection (simulated)
    if "cat" in name:
        objects.append("a cat")
        actions.append("sitting")

    if "dog" in name:
        objects.append("a dog")
        actions.append("playing")

    if "car" in name:
        objects.append("a car")
        actions.append("parked")

    if "tree" in name:
        objects.append("a tree")

    if "person" in name or "man" in name or "woman" in name:
        objects.append("a person")
        actions.append("standing")

    if "flower" in name:
        objects.append("flowers")

    # Caption generation logic
    if objects:
        caption = " and ".join(objects)

        if actions:
            caption += " is " + " and ".join(actions)

        return caption.capitalize() + "."

    return "An image with various objects."

# Main program
print("📷 AI Image Caption Generator (No Libraries)")
image_name = input("Enter image file name: ")

caption = generate_caption(image_name)

print("\n📝 Generated Caption:")
print(caption)