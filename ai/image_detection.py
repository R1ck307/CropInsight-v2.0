def analyze_image(image, crop):

    """
    Placeholder AI image detection engine.
    Later this can be replaced with a trained model.
    """


    crop = crop.lower()


    predictions = {


        "tomato": [
            {
                "disease": "Early Blight",
                "confidence": 82
            },
            {
                "disease": "Leaf Mold",
                "confidence": 65
            }
        ],


        "maize": [
            {
                "disease": "Leaf Blight",
                "confidence": 78
            },
            {
                "disease": "Rust",
                "confidence": 60
            }
        ],


        "beans": [
            {
                "disease": "Angular Leaf Spot",
                "confidence": 75
            }
        ]

    }



    if crop in predictions:

        return predictions[crop]


    return [
        {
            "disease": "Unknown",
            "confidence": 40
        }
    ]
