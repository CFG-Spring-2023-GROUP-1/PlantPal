import React from 'react';
import { DetailsCard, TitleCard } from '../../../components/cards';
import { plant } from '../../../utils/constants';
import BackButton from '../../../components/base/back-button';

const PlantDetails = () => {
  return (
    <div className='space-y-8'>
      <BackButton />
      <TitleCard text='Plant Details'>
        <div className='grid grid-cols-4 gap-y-12 py-6'>
          <DetailsCard details={plant?.CommonNames} title='Common Names' />
          <DetailsCard details={plant?.LatinName} title='Latin Name' />
          <DetailsCard details={plant?.Category} title='Category' />
          <DetailsCard details={plant?.LightLevel} title='Ideal Light' />
          <DetailsCard details={plant?.LeafColour} title='Leaf Color' />
          <DetailsCard details={plant?.BloomingSeason} title='Blooming Season' />
          <DetailsCard details={plant?.Climate} title='Climate' />
          <DetailsCard details={plant?.GrowthSpeed} title='GrowthSpeed' />
          <DetailsCard details={plant?.CommonDiseases} title='Common Diseases' />
          <DetailsCard details={plant?.BloomingSeason} title='Blooming Season' />
          <DetailsCard details={plant?.Perfume} title='Perfume' />
          <DetailsCard details={plant?.ColourOfBloom} title='Color Of Bloom' />
          <DetailsCard details={plant?.Watering} title='Care Instructions' />
          <DetailsCard details={plant?.PlantDescription} title='Plant Description' />
        </div>
      </TitleCard>
    </div>
  );
};

export default PlantDetails;
