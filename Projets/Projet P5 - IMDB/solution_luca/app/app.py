from flask import Flask, render_template, request
from joblib import load
from preprocessing.inference_preprocessing import prepare_data

app = Flask(__name__)

@app.before_first_request
def load_model():
  global model
  global scaler
  print('loading model and scaler...')
  model = load('model/xgb_model.joblib')
  scaler = load('model/min_max_scaler.joblib')
  print('model and scaler loaded!')


@app.route('/')
def home():
    return "access /predict to run a prediction"


# On reçoit un JSON, et on renvoit un JSON
@app.route('/predict', methods=['POST'])
def predict():
  if request.method == 'POST':

      df_to_predict = prepare_data(request.json, scaler)

      predictions = model.predict(df_to_predict).tolist()
      predictions_dict = {}
      predictions_dict['predictions'] = predictions

  return predictions_dict


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
