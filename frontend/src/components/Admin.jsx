import Navbar from "./Navbar";
import { useNavigate } from "react-router-dom";

const Admin = () => {
  const navigate = useNavigate();
  const autos = [
    { id: 1, marca: "Toyota", modelo: "Corolla", año: 2020 },
    { id: 2, marca: "Ford", modelo: "Fiesta", año: 2018 },
    { id: 3, marca: "Chevrolet", modelo: "Onix", año: 2021 },
  ];

  return (
    <>
      <Navbar />
      <div className="min-h-screen bg-gray-100 p-6">
        <div className="max-w-5xl mx-auto">
          <h1 className="text-3xl font-bold mb-6 text-center">
            Panel de Administrador
          </h1>

          <div className="flex flex-wrap gap-4 justify-center mb-8">
            <button className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition hover:cursor-pointer">
              Agregar Auto
            </button>
            <button className="bg-yellow-500 text-white px-4 py-2 rounded-lg hover:bg-yellow-600 transition hover:cursor-pointer">
              Editar Auto
            </button>
            <button className="bg-red-600 text-white px-4 py-2 rounded-lg hover:bg-red-700 transition hover:cursor-pointer">
              Eliminar Auto
            </button>
          </div>

          <h2 className="text-xl font-semibold mb-4">Autos Publicados</h2>
          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {autos.map((auto) => (
              <div key={auto.id} className="bg-white p-4 rounded-lg shadow-md">
                <h3 className="text-lg font-bold">
                  {auto.marca} {auto.modelo}
                </h3>
                <p className="text-gray-600">Año: {auto.año}</p>
                <div className="mt-2 text-sm text-gray-400">ID: {auto.id}</div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </>
  );
};

export default Admin;
