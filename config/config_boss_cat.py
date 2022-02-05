amount_of_nfts = 50

config = {
  "layers": [
    {
      "name": "Background",
      "values": ["Green", "Pink", "Blue", "Cyan", "Light Blue", "Orange", "Pastelle Orange", "Pastelle Pink", "Purple", "Yellow"],
      "trait_path": "./trait-layers/background",
      "filename": ["green", "pink", "blue", "cyan", "light_blue", "orange", "pastelle_orange", "pastelle_pink", "purple", "yellow"],
      "weights": [10,10,10,10,10,10,10,10,10,10]
    },
    {
      "name": "Round Object",
      "values": ["Basketball", "Coin", "Football", "Globe", "Soccer Ball"],
      "trait_path": "./trait-layers/round_object",
      "filename": ["basketball", "coin", "football", "globe", "soccer-ball"],
      "weights": [20,20,20,20,20]
    },
    {
      "name": "Boss Cat",
      "values": ["Boss Cat"],
      "trait_path": "./trait-layers/boss_cat",
      "filename": ["boss-cat"],
      "weights": [100]
    }
  ],
  "incompatibilities": [
    
  ],
  "baseURI": ".",
  "name": "NFT #",
  "description": "This is a description for this NFT series."
}