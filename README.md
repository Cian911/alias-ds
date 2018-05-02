### Install & Dependencies

Install dlib
`pip3 install dlib`

Install python boost
`sudo apt-get install libboost-all-dev`

TensorFlow & TFLearn & TF GPU Support
`pip3 install tensorflow` - `pip3 install tensorflow-gpu` - `pip3 install tflearn`

Facial Recognition Library
`pip3 install face_recognition`

## Steps - Facial Detection

 - Find Faces in picture
 - Define uniuqe facial features and get face landmarks
 - Store Face Landmarks
 - Compare facial features against other profile images
 - Build and serve score based on findings

## Steps - Profile Score

  - Download alias/ioCMS confirmed contact suggestions
  - Train model based on this
  - Add weighted attribtes to network nodes

---

### Alias ML Sample Data
---
Platforms
  - Twitter *
  - Facebook
  - Instagram
  - Youtube

`*` Denotes the original platform the search is being performed on.

#### Unified Response Information from Individual Platforms
---
```
{
  twitter: {
    email: 'cian@ciangallagher.net',
    phone: '08512345643',
    thumnail_hashes: 'http://img.thumbnail.twitter.com/33243242343242.png',
    city: 'Dublin, Ireland'
  }
}
```
