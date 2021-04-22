from PIL import Image
from PIL.ExifTags import TAGS

def metadata_extractor: 
    
    def extractor(image_file_name):

        # open the image
        image = Image.open(image_file_name)
        # extracting the exif metadata
        print(image.size)
        print(image.mode)
        print(image.format)
        exifdata = image.getexif()
        # add values to dict as key value pairs
        values = {}
        values.update({"format": image.format})
        values.update({"size": image.size})
        values.update({"mode": image.mode})
        # looping through all the tags present in exifdata
        for tagid in exifdata:   
            # getting the tag name instead of tag id
            tagname = TAGS.get(tagid, tagid)
            # passing the tagid to get its respective value
            value = exifdata.get(tagid)
            # printing the final result
            print(f"{tagname:25}: {value}")
            values.update({str(tagname): value})

        print(values)
        with open("C:/Users/awyon/Documents/PythonProjekt/exextract/data.csv", "w") as metadata:
            for key in values.keys():
                metadata.write("%s,%s\n" % (key, values[key]))
