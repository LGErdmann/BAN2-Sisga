import React from 'react';

import CustomNavbar from '../../components/CustomNavbar';

const Null = () => {
  return (
    <>
    <CustomNavbar />
    <div 
    style={{
      display: "flex",
      width: "100vw",
      height: "100vh",
      justifyContent: "center",
      alignItems: "center"
    }}>
      <h1>
        Esta pagina não existe
      </h1>
    </div>
      
    </>
  );
}

export default Null;
