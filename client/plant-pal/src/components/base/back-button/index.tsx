import React from 'react';
import { BiArrowBack, BiLeftArrowCircle } from 'react-icons/bi';
import { BsBack } from 'react-icons/bs';
import { useNavigate } from 'react-router-dom';

type BackButtonColor = 'red' | 'gray';

const BackButton = ({
  link,
  text = 'Back',
  onClick
}: {
  link?: string;
  text?: string;
  color?: BackButtonColor;
  onClick?: () => void;
}) => {
  const navigate = useNavigate();
  const goBack = () => {
    if (link) {
      navigate(link);
    } else if (onClick) {
      onClick?.();
    } else {
      navigate(-1);
    }
  };
  return (
    <div
      className={`cursor-pointer flex gap-2 items-center text-xs uppercase font-semibold mb-3 text-green-700`}
      onClick={goBack}>
      <BiLeftArrowCircle size={14} />
      <span>{text}</span>
    </div>
  );
};

export default BackButton;
