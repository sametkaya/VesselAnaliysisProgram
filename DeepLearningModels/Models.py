from torchvision.transforms import functional as F


from DeepLearningModels.unet import *
from PIL import Image
import torch

def Segment(imagePath):

    image = Image.open(imagePath).convert("L")

    resize = torch.nn.functional.interpolate
    input_image = F.to_tensor(image).unsqueeze(0)
    input_image = resize(input_image, size=(512, 512))

    current_directory = os.path.dirname(os.path.abspath(__file__))
    model_file_path = os.path.join(current_directory, "model_unet.pt")

    # Unet model creating
    model = build_unet()
    model.load_state_dict(torch.load(model_file_path, map_location=torch.device('cpu')))
    model.eval()

    # Segmentation with model
    with torch.no_grad():
        segmented_output = model(input_image)


    segmented_output = torch.sigmoid(segmented_output)  # Sigmoid aktivasyonu
    segmented_output = (segmented_output > 0.5).float()  # Thresholding
    segmented_output = F.to_pil_image(segmented_output[0])

    """
    resampling_filter = Image.LANCZOS  

    # Yeniden boyutlandırma işlemi
    #segmented_output = segmented_output.resize((512, 512), resampling_filter)

    """

    # Save output image
    #segmented_output.show()

    filename_without_extension, _ = os.path.splitext(imagePath)
    filename_without_extension, _ = os.path.splitext(imagePath)
    segmented_file_path = filename_without_extension + "_segmented.png"
    segmented_output.save(segmented_file_path)

    return segmented_file_path

