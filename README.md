# Setup libraries:

### MACOSX:

#### TTS:
```
brew install espeak
pip install pyttsx3
```

#### ASR:
```
pip3 install SpeechRecognition
pip3 install pyaudio
pip3 install google-api-python-client
pip3 install gcloud
pip3 install pocketsphinx
pip3 install PyAudio
```
Setup your Google Cloud Account and set the environment variable GOOGLE_APPLICATION_CREDENTIALS (add it on bash_profile!!) to the file path of the JSON file that contains your service account key:
https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries

Troubleshooting ```pip3 install pocketsphinx```:
https://github.com/bambocher/pocketsphinx-python/issues/28

