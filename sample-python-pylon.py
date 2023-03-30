from pypylon import pylon

# Initialize the Pylon runtime system
pylon.pylon_initialize()

try:
    # Create a camera object and attach to the first available camera
    camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

    # Start the camera
    camera.Open()
    camera.StartGrabbing()

    # Grab and process images
    for i in range(10):
        # Wait for the next image
        grab_result = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

        # Check if the image is valid
        if grab_result.GrabSucceeded():
            # Access the image data
            data = grab_result.Array
            width = grab_result.Width
            height = grab_result.Height
            pixel_format = grab_result.PixelType

            # Process the image data here...

            # Display the image size and pixel format
            print(f"Image width: {width}")
            print(f"Image height: {height}")
            print(f"Pixel format: {pixel_format}")

finally:
    # Stop the camera and close it
    camera.StopGrabbing()
    camera.Close()

    # Terminate the Pylon runtime system
    pylon.pylon_terminate()
