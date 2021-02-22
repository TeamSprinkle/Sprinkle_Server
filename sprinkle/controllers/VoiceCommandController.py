"""
  VoiceCommandComtroller.py
  Sprinkle

  Created by LeeKW on 2021/02/19.
"""

# from sprinkle.models.VoiceCommand import User
from kochat.app import KochatApi
from kochat.app import KochatApi
from kochat.data import Dataset
from kochat.loss import CRFLoss, CosFace, CenterLoss, COCOLoss, CrossEntropyLoss
from kochat.model import intent, embed, entity
from kochat.proc import DistanceClassifier, GensimEmbedder, EntityRecognizer, SoftmaxClassifier

from sprinkle.scenrios import call, schedule

dataset = Dataset(ood=True)
emb = GensimEmbedder(model=embed.FastText())

clf = DistanceClassifier(
    model=intent.CNN(dataset.intent_dict),
    loss=CenterLoss(dataset.intent_dict),
)

rcn = EntityRecognizer(
    model=entity.LSTM(dataset.entity_dict),
    loss=CRFLoss(dataset.entity_dict)
)

kochat = KochatApi(
    dataset=dataset,
    embed_processor=(emb, False),
    intent_classifier=(clf, False),
    entity_recognizer=(rcn, False),
    scenarios=[
        call, schedule
    ]
)

class VoiceCommandController():
    def __init__(self):
        # self.voiceCommand = User()
        print("")

    def test(self, text):
    
        prep = kochat.dataset.load_predict(text, kochat.embed_processor)
        intent = kochat.intent_classifier.predict(prep, calibrate=False)
        entity = kochat.entity_recognizer.predict(prep)
        text = kochat.dataset.prep.tokenize(text, train=False)
        # KochatApi.dialogue_cache[uid] = KochatApi.scenario_manager.apply_scenario(intent, entity, text)
        
        print(intent)
        print(entity)
        print(text)

        return "aa"
    