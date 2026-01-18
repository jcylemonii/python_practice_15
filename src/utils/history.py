import matplotlib.pyplot as plt
import typing

def save_history_loss(loss: typing.Any, file_path: str): 
    loss_epochs = range(1, len(loss) + 1)

    _, ax = plt.subplots()
    ax.plot(loss_epochs, loss, "b-", label="Training loss")
    ax.set_title("Training loss")
    ax.set_xlabel("Epochs")
    ax.set_ylabel("Loss")
    plt.savefig(file_path)

def save_history_accuracy(accuracy: typing.Any, file_path: str): 
    acc_epochs = range(1, len(accuracy) + 1)

    _, ax = plt.subplots()
    ax.plot(acc_epochs, accuracy, "b-", label="Training accuracy")  
    ax.set_title("Training accuracy")
    ax.set_xlabel("Epochs")
    ax.set_ylabel("Accuracy")
    plt.savefig(file_path)