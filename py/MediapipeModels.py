#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mediapipe as mp

class MediapipeHandModel:
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands

        self.hand_model = self.mp_hands.Hands(static_image_mode=True,
            max_num_hands=2,
            min_detection_confidence=0.5)
        
    def return_mp_drawing(self):
        return self.mp_drawing
    
    def return_mp_drawing_styles(self):
        return self.mp_drawing_styles
    
    def return_mp_hands(self):
        return self.mp_hands
        
    def return_hand_model(self):
        return self.hand_model


# In[ ]:




