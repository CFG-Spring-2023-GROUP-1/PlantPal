export type TempType = { 
  Celsius: string | number,
  Fahrenheit: string | number,
}

export type PlantType = {
  PlantId: string,
  Category: string,
  LatinName: string,
  CommonNames: string,
  LightLevel: string,
  Climate: string,
  MaxTemp: TempType,
  MinTemp: TempType,
  Watering: string,
  GrowthSpeed: string,
  CommonDiseases: string,
  PlantDescription: string,
  LeafColour: string,
  BloomingSeason: string,
  Perfume: string,
  ColourOfBloom: string,
  Image: string,
}
