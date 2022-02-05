amount_of_nfts = 11

config = {
  "layers": [
    {
      "name": "Background",
      "values": ["Blue", "Orange", "Purple", "Red", "Yellow"],
      "trait_path": "./trait-layers/backgrounds",
      "filename": ["blue", "orange", "purple", "red", "yellow"],
      "weights": [20,20,20,20,20]
    },
    {
      "name": "Foreground",
      "values": ["Python Logo", "Python Logo 32"],
      "trait_path": "./trait-layers/foreground",
      "filename": ["logo", "logo"],
      "weights": [50, 50]
    },
    {
      "name": "Branding",
      "values": ["A Name", "Another Name"],
      "trait_path": "./trait-layers/text",
      "filename": ["text", "text"],
      "weights": [50, 50]
    }
  ],
  "incompatibilities": [
    {
      "layer": "Background",
      "value": "Blue",
      "incompatible_with": ["Python Logo 2"]
    },  #  @dev : Blue backgrounds will never have the attribute "Python Logo 2".
  ],
  "baseURI": ".",
  "name": "NFT #",
  "description": "This is a description for this NFT series."
}