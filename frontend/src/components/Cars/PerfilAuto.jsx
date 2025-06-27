import { useParams } from "react-router-dom";
import Navbar from "../Navbar/Navbar";
import { useEffect, useState } from "react";

const PerfilAuto = () => {
  const { id } = useParams();
  const [auto, setAuto] = useState(null);

  useEffect(() => {
    const obtenerAuto = async () => {
      const respuesta = await fetch(`http://localhost:8000/autos/${id}`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });
      const data = await respuesta.json();
      setAuto(data);
    };

    obtenerAuto();
  }, [id]);

  if (!auto) {
    return <p className="text-center mt-10">Cargando auto...</p>;
  }

  return (
    <>
      <Navbar />
      <div className="min-h-screen bg-gradient-to-br from-gray-800 to-blue-600 p-4">
        <div className="max-w-6xl mx-auto p-6 mt-10">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-10 bg-white shadow-lg rounded-lg p-6">
            <div className="w-full h-80 md:h-full">
              <img
                src={`http://localhost:8000${auto.imagen}`}
                alt={auto.nombre}
                className="object-cover w-full h-full rounded-lg"
              />
            </div>

            <div className="flex flex-col justify-between">
              <div>
                <h2 className="text-3xl font-bold text-gray-800 mb-2">
                  {auto.nombre}
                </h2>
                <p className="text-gray-600 mb-2">
                  Marca:{" "}
                  <span className=" capitalize font-semibold">
                    {auto.marca_id}
                  </span>
                </p>
                <p className="text-gray-600 mb-4">
                  Modelo:{" "}
                  <span className=" capitalize font-semibold">
                    {auto.modelo_id}
                  </span>
                </p>
                <p className="text-gray-600 mb-4">
                  Estado:{" "}
                  <span className="capitalize font-semibold">
                    {auto.estado_id}
                  </span>
                </p>
                <p className="text-gray-600 mb-4">
                  Color:{" "}
                  <span className="capitalize font-semibold">
                    {auto.color_id}
                  </span>
                </p>
              </div>

              <button className="mt-6 bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-500 transition">
                Contactar vendedor
              </button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default PerfilAuto;
