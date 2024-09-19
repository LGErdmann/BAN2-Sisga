import React from 'react';

import CustomNavbar from '../../components/CustomNavbar';
import CardContainer from '../../components/home/CardContainer';

const Home = () => {
  const valores = [
    {
      titulo: "Coordenadores",
      total: "5"
    },
    {
      titulo: "Professores",
      total: "10"
    },
    {
      titulo: "Alunos",
      total: "20"
    },
    {
      titulo: "Cursos",
      total: "5"
    },
    {
      titulo: "Disciplinas",
      total: "10"
    },
    {
      titulo: "Salas",
      total: "10"
    },
  ]

  return (
    <>
      <CustomNavbar />
      <CardContainer valores={valores}/>

    </>
  );
}

export default Home;
