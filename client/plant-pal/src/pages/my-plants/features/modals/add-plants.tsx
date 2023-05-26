import React, { useState } from 'react';
import BaseModal from '../../../../components/base/modal';
import { Input } from '../../../../components/base/input';
import Button from '../../../../components/base/button';
import { BsSearch } from 'react-icons/bs';
import { apiService } from '../../../../services/base.service';
import { PlantSuggestionCard } from '../../../../components/cards';
import BackButton from '../../../../components/base/back-button';
import Loader from '../../../../components/base/loader';
import AddPrompt from './add-prompt';

export type PlantSuggestionType = {
  id: string;
  Name: string[];
  latinName: string;
  Category: string;
  Img: string;
};
const AddPlantsModal = ({ show, onClose }: { show: boolean; onClose: () => void }) => {
  const [plantName, setPlantName] = useState('');
  const [step, setStep] = useState(0);
  const [loading, setLoading] = useState(false);
  const [showPrompt, setShowPrompt] = useState(false);
  const [plantSuggestions, setPlantSuggestions] = useState([] as PlantSuggestionType[]);
  const [selectedPlant, setSelectedPlant] = useState({} as PlantSuggestionType);
  const getPlantsSuggestions = async () => {
    setLoading(true);
    try {
      const res = await apiService.get('search', { query: plantName }, false, false, true);
      const response = res?.data;
      if (response) {
        setStep(step + 1);
        let suggestions: PlantSuggestionType[] = [];
        response?.map((item: any) => {
          return (suggestions = suggestions.concat({
            id: item?.item?.id,
            Name: item?.item['Common name'],
            Category: item?.item['Categories'],
            Img: item?.item['Img'],
            latinName: item?.item['Latin name']
          }));
        });
        console.log(suggestions);
        setPlantSuggestions(suggestions);
      }
    } catch (err) {
      console.log(err);
    } finally {
      setLoading(false);
    }
  };

  const toggleShowPrompt = () => {
    setShowPrompt(!showPrompt);
  };
  const handleClick = (item: PlantSuggestionType) => {
    setSelectedPlant(item);
    toggleShowPrompt();
  };
  return (
    <div>
      <BaseModal
        show={show}
        onClose={onClose}
        wide={step == 1}
        title={step === 0 ? 'Add A' : step === 1 ? 'Add To ' : ''}
        coloredText={step === 0 ? 'Plant' : step === 1 ? 'My Plants' : ''}>
        {step == 0 ? (
          <div className='space-y-12'>
            <Input
              name={'name'}
              label='Plant Name'
              onChange={(e) => setPlantName(e.target.value)}
              placeholder='search by common or latin name'
            />
            <Button
              color='green'
              loading={loading}
              className='flex items-center gap-2 justify-end ml-auto'
              onClick={getPlantsSuggestions}>
              <BsSearch />
              Search
            </Button>
          </div>
        ) : step === 1 && loading ? (
          <Loader />
        ) : (
          <div className='shadow-md rounded-2xl bg-white p-5 Y'>
            <BackButton onClick={() => setStep(step - 1)} />
            <div className='flex flex-wrap gap-4 gap-y-8 justify-around h-[380px] overflow-scroll no-scroll-bar'>
              {plantSuggestions?.map((item, i) => (
                <PlantSuggestionCard key={i} list={item} onClick={() => handleClick(item)} />
              ))}
            </div>
          </div>
        )}
      </BaseModal>

      <AddPrompt show={showPrompt} onClose={toggleShowPrompt} item={selectedPlant} />
    </div>
  );
};

export default AddPlantsModal;
