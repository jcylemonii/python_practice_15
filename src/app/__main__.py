import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utils.files import download_file
from utils.history import save_history_loss, save_history_accuracy
from os.path import exists
from keras import Input
from keras.models import Model
from keras.layers import Dense
from keras.utils import to_categorical


def main():

    resource = "https://storage.yandexcloud.net/academy.ai/A_Z_Handwritten_Data.csv"
    destination = "./src/datasets/A_Z_Handwritten_Data.csv"

    if exists(destination) is False:
        print(f"The file does not exist at {destination}")
        download_file(resource, destination)
    else:
        print(f"The file already exists at {destination}")

    # Load the dataset
    df = pd.read_csv(destination)

    # Labels
    labels = df.iloc[:, 0].values
    num_classes = 26 # A-Z letters
    labels_ctg = to_categorical(labels, num_classes)

    # Do reshaping + 0-1 normalization
    df_reshaped = df.iloc[:, 1:].values
    df_reshaped = df_reshaped.reshape(-1, 28, 28)
    df_reshaped = df_reshaped.astype("float32") / 255.0

    # Define layers
    input_layer = Input(shape=(28 * 28,))
    hidden_1 = Dense(256, "relu")(input_layer)
    hidden_2 = Dense(128, "relu")(hidden_1)
    hidden_3 = Dense(64, "relu")(hidden_2)
    output_layer = Dense(num_classes, "softmax")(hidden_3)

    # Connect layers to the model
    model = Model(inputs=input_layer, outputs=output_layer)

    # Compile the model
    model.compile(
        optimizer="rmsprop",
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )

    # Train dataframes
    history = model.fit(
        df_reshaped.reshape(-1, 28 * 28),
        labels_ctg,
        epochs=3,
        batch_size=128,
    )

    # Create image of the plot with accuracy
    history_dict = history.history

    save_history_accuracy(history_dict["accuracy"], "./src/imgs/accuracy.png")
    save_history_loss(history_dict["loss"], "./src/imgs/loss.png")

    # Select a sample for prediction 
    sample = df_reshaped[30002] # C = 2
    sample = sample.reshape(1, 28 * 28)

    # Prediction result
    prediction = model.predict(sample)
    value = np.argmax(prediction)

    print(f"Predicted class for the first sample: {value}")

if __name__ == "__main__":
    main()
