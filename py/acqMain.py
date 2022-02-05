#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sys
import argparse
import numpy


# In[13]:


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--Model", type=str,required=True, help = "Select Model name. From more info visit GitHub page.")
    parser.add_argument("-t", "--Type", type=str,required=True, help = "Select Model type. From more info visit GitHub page.")

    args = parser.parse_args((' '.join(sys.argv[1:])).split())
    
    if args.Model and args.Type:
        process(args.Model,args.Type)
    
def process(m_name,m_type):
    from acqInterface import Interface
    g = Interface('python acquisition tool',600,400)
    if m_name == "Mediapipe": g.set_mediapipe_model(m_type)
    g.__initGUI__()
    
if __name__ == '__main__':
    main()


# In[ ]:




