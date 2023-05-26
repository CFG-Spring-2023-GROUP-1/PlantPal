import React from 'react';
import { PlantCard } from '../../../components/cards';
import Img from '../../../assets/img/login.jpg';
import Img2 from '../../../assets/img/plant-pot.jpg';
import Button from '../../../components/base/button';
import { IoMdAddCircleOutline } from 'react-icons/io';
import { useNavigate } from 'react-router-dom';
import { ROUTE_KEYS } from '../../../utils/constants';

const MyPlantFriend = () => {
  const navigate = useNavigate();

  const getPlantDetails = (item: string) => {
    navigate(`${ROUTE_KEYS.PLANTS}/${item}`);
  };
  return (
    <div className='space-y-10'>
      <div className='flex justify-between'>
        <h4>Plant Tips & Tutorials</h4>
      </div>
      <div className='grid grid-cols-3 gap-10'>
        <PlantCard
          onClick={() => getPlantDetails('123')}
          Img={Img}
          details={'Find tips and tutorials on watering'}
          title='watering'
        />
        <PlantCard
          onClick={() => getPlantDetails('123')}
          Img={Img2}
          details={'Find tips and tutorials on fertilizing'}
          title='fertilizing'
        />
      </div>
    </div>
  );
};

export default MyPlantFriend;
