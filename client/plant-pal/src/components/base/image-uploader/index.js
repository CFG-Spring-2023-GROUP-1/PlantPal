import React, { useRef } from 'react';
import { BiPlus } from 'react-icons/bi';
import { FiEdit } from 'react-icons/fi';
import { ReactComponent as ImageIcon } from '../../../assets/img/image.svg';

const ImgUploader = ({ file, onFileChange, isEdit }) => {
  const inputRef = useRef(null);
  return (
    <div className=' flex items-center flex-wrap gap-4'>
      <div
        className={`w-12 h-12 md:w-20 md:h-20 rounded-full flex items-center justify-center relative ${
          isEdit ? 'border border-yellow-100' : 'bg-white-100'
        }`}>
        {!file && <ImageIcon />}
        {file && <img src={file} alt='' className='w-[90%] h-[90%] rounded-full' />}
        <div className='bg-pink-100 w-6 h-6 absolute rounded-full right-0 bottom-0 text-white-100 items-center flex justify-center cursor-pointer'>
          {isEdit ? (
            <FiEdit size={12} onClick={() => inputRef?.current?.click()} />
          ) : (
            <BiPlus onClick={() => inputRef?.current?.click()} />
          )}
        </div>
        <input
          ref={inputRef}
          type={'file'}
          hidden
          onChange={onFileChange}
          accept='image/png, image/gif, image/jpeg'
        />
      </div>

      {!isEdit && (
        <div className=' flex flex-col gap-2'>
          <h6 className='font-semibold'>ADD A PROFILE IMAGE</h6>
          <p className='text-[#595959] text-2xs'>
            *Not more than 30kb | Accepts jpg, .png, .gif
            <br /> *Recommended dimensions: 200px X 200px
          </p>
        </div>
      )}
    </div>
  );
};

export default ImgUploader;
