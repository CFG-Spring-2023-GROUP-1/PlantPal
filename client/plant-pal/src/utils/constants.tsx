import React from 'react';
import { GiPlantSeed } from 'react-icons/gi';
import { BiCalendarEvent } from 'react-icons/bi';
import { BsPeople } from 'react-icons/bs';
import { FiHelpCircle } from 'react-icons/fi';
import { PlantType } from './types';

export const STORAGE_KEYS = {
  USER_ID: 'id',
  EMAIL: 'email',
  FIRST_NAME: 'first_name',
  LAST_NAME: 'last_name'
};

export const ROUTE_KEYS = {
  LOGIN: '/login',
  REGISTER: '/register',
  HOME: '/',
  MY_PLANTS: '/my-plants',
  PlANT_DETAILS: ':id',
  PLANT_FRIEND: '/my-plant-friend',
  PlANT_FRIEND_DETAILS: ':id'
};

export const SIDE_BAR = [
  {
    icon: <GiPlantSeed size={22} />,
    title: 'my plants',
    route: ROUTE_KEYS.MY_PLANTS
  },
  {
    icon: <FiHelpCircle size={22} />,
    title: 'my plant suggestions',
    route: ROUTE_KEYS.MY_PLANTS
  },
  {
    icon: <BiCalendarEvent size={22} />,
    title: 'my plant calender',
    route: ROUTE_KEYS.MY_PLANTS
  },
  {
    icon: <BsPeople size={22} />,
    title: 'my plant friend',
    route: ROUTE_KEYS.PLANT_FRIEND
  }
];
export const plant: PlantType = {
  PlantId: 'PL001',
  Category: 'Indoor',
  LatinName: 'Monstera deliciosa',
  CommonNames: 'Swiss cheese plant, Split-leaf philodendron',
  LightLevel: 'Medium to bright indirect light',
  Watering: 'Water thoroughly, then allow the top inch of soil to dry out before watering again',
  Climate: 'Tropical',
  MaxTemp: {
    Celsius: 30,
    Fahrenheit: 86
  },
  MinTemp: {
    Celsius: 18,
    Fahrenheit: 64
  },
  GrowthSpeed: 'Moderate',
  CommonDiseases: 'Root rot, Leaf spot',
  PlantDescription:
    'Monstera deliciosa is a popular tropical houseplant known for its large, glossy, and fenestrated leaves. It is relatively easy to care for and adds a touch of exotic beauty to any indoor space.',
  LeafColour: 'Green',
  BloomingSeason: 'Spring to summer',
  Perfume: 'None',
  ColourOfBloom: 'White',
  Image: 'https://example.com/plant001.jpg'
};
