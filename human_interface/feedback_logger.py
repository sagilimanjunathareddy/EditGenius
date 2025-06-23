def log_feedback(text, file_path="feedback.log"):
    with open(file_path, 'a') as f:
        f.write(text + "\n")