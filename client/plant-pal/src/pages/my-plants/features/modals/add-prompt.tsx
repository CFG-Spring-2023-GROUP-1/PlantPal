import React, { useState } from 'react';
import Button from '../../../../components/base/button';
import { PlantSuggestionType } from './add-plants';
import BaseModal from '../../../../components/base/modal';

const AddPrompt = ({
  show,
  onClose,
  item
}: {
  show: boolean;
  onClose: () => void;
  item: PlantSuggestionType;
}) => {
  const [loading, setLoading] = useState(false);

  const addPlant = () => {
    //
  };
  return (
    <BaseModal
      show={show}
      onClose={onClose}
      title={`Are you sure you want to add ${item?.latinName} to`}
      coloredText={'My Plants'}>
      <div className=' flex mx-auto justify-between'>
        <Button
          color='green'
          loading={loading}
          className=' bg-white text-black'
          onClick={() => onClose()}>
          <p className='text-black'>Cancel</p>
        </Button>
        <Button color='green' loading={loading} className='' onClick={addPlant}>
          Confirm
        </Button>
      </div>
    </BaseModal>
  );
};

export default AddPrompt;
