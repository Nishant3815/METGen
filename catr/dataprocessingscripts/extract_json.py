import csv
import json

def make_json(csvFilePath, jsonFilePath):
    # create a dictionary
    data = {"annotations":[], "images": []}

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary
        # and add it to data
        index = 1
        for rows in csvReader:
            # Assuming a column named 'No' to
            # be the primary key
            # print(rows)
            caption = rows["comment"]
            image_id = rows["image_hash"]
            data["annotations"].append({"id": index, "caption": caption, "image_id": image_id})
            index+=1

    # Open a json writer, and use the json.dumps()
    # function to dump data

    print(data)
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


# Driver Code

# Decide the two file paths according to your
# computer system
csvFilePath = r'test_caption.csv'
jsonFilePath = r'caption_test.json'

# Call the make_json function
make_json(csvFilePath, jsonFilePath)