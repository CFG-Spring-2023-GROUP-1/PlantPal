import moment from "moment/moment";
import React from "react";
import { CgProfile } from "react-icons/cg";

const NavBar = () => {

  const currentDate = moment(new Date()).format("dddd, MMMM YYYY, LT")

  return (
    <div className=" p-4 bg-brown-100 w-full flex gap-6 flex-wrap items-center justify-between text-green-700">
      <p className=" font-bold text-lg capitalize "> Hello, Emina.</p>

      <div className="flex gap-5 items-center">
        <p className=" font-medium capitalize"> {currentDate} </p>
        <CgProfile size={20} />
      </div>

    </div>
  );
};

export default NavBar;
