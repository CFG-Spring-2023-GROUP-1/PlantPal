import React, { useState } from 'react';
import { PlantCard } from '../../../components/cards';
import Img from '../../../assets/img/login.jpg';
import Img2 from '../../../assets/img/plant-pot.jpg';
import Button from '../../../components/base/button';
import { IoMdAddCircleOutline } from 'react-icons/io';
import { useNavigate } from 'react-router-dom';
import { ROUTE_KEYS } from '../../../utils/constants';
import AddPlantsModal from './modals/add-plants';

const MyPlants = () => {
  const [showAddPlantModal, setShowAddPlantModal] = useState(false);
  const navigate = useNavigate();

  const getPlantDetails = (item: string) => {
    navigate(`${ROUTE_KEYS.PLANTS}/${item}`);
  };

  const addPlants = () => {
    setShowAddPlantModal(!showAddPlantModal);
  };

  return (
    <div className='space-y-10'>
      <div className='flex justify-between items-center'>
        <h4>My Plants</h4>
        <Button
          color='green'
          className='flex items-center max-w-[200px] justify-center gap-2'
          onClick={addPlants}>
          <IoMdAddCircleOutline size={14} />
          <p> Add A Plant</p>
        </Button>
      </div>
      <div className='grid grid-cols-3 gap-10'>
        <PlantCard
          onClick={() => getPlantDetails('123')}
          Img={Img}
          details={'Water thoroughly, then allow the top inch of soil to dry out'}
          title='Swiss cheese plant'
        />
        <PlantCard
          onClick={() => getPlantDetails('123')}
          Img={Img2}
          details={
            'Water thoroughly, then allow the top inch of soil to dry out before watering again Water thoroughly, then allow the top inch of soil to dry out before watering again'
          }
          title='Swiss cheese plant'
        />
        <PlantCard
          onClick={() => getPlantDetails('123')}
          Img={Img}
          details={'Water thoroughly, then allow the top inch of soil to dry out'}
          title='Monstera deliciosa'
        />
        <PlantCard
          onClick={() => getPlantDetails('123')}
          Img={Img2}
          details={'flko'}
          title='Swiss cheese plant'
        />
        <PlantCard
          onClick={() => getPlantDetails('123')}
          Img={Img}
          details={
            'Water thoroughly, then allow the top inch of soil to dry out before watering again'
          }
          title='Swiss cheese plant'
        />
        <PlantCard
          onClick={() => getPlantDetails('123')}
          Img={Img2}
          details={'flko'}
          title='Swiss cheese plant'
        />
      </div>
      <AddPlantsModal show={showAddPlantModal} onClose={addPlants} />
    </div>
  );
};

export default MyPlants;
