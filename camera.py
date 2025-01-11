import cv2
import tensorflow as tf

MODEL_PATH = "ai_model/model_file.h5"
model = tf.keras.models.load_model(MODEL_PATH)

def analyze_camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break
        
        # Preprocess the frame for AI model
        resized_frame = cv2.resize(frame, (224, 224))  # Adjust based on your model's input size
        preprocessed_frame = resized_frame / 255.0
        prediction = model.predict(preprocessed_frame.reshape(1, 224, 224, 3))
        
        # Display the prediction
        cv2.imshow("Camera Feed", frame)
        print(f"Prediction: {prediction}")
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
