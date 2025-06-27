import { useEffect } from "react";
import Navbar from "../components/Navbar/Navbar";
import { useNavigate } from "react-router-dom";
import { useState } from "react";

const Admin = () => {
  const navigate = useNavigate();
  const [autos, setAutos] = useState([]);

  const getAutos = async () => {
    const token = localStorage.getItem("token");
    const response = await fetch("http://localhost:8000/autos/", {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    const data = await response.json();
    setAutos(data);
    console.log(data);
  };

  const handleDelete = async (id) => {
    const token = localStorage.getItem("token");

    const request = await fetch(`http://localhost:8000/autos/?auto=${id}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
    });
    const response = await request.json();

    if (response == "Borrado con éxito") {
      alert("Auto eliminado exitosamente");
      getAutos();
    } else {
      alert("Error al eliminar el auto: " + response.message);
    }
  };

  useEffect(() => {
    getAutos();
  }, []);

  return (
    <>
      <Navbar />
      <div className="min-h-screen bg-gray-100 p-6">
        <div className="max-w-5xl mx-auto">
          <h1 className="text-3xl font-bold mb-6 text-center">
            Panel de Administrador
          </h1>

          <div className="flex flex-wrap gap-4 justify-center mb-8">
            <button
              onClick={() => navigate("/admin/crear-auto")}
              className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition hover:cursor-pointer"
            >
              Agregar Auto
            </button>
          </div>

          <h2 className="text-xl font-semibold mb-4">Autos Publicados</h2>
          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {autos.map((auto) => (
              <div
                key={auto.id}
                className="bg-white p-4 rounded-lg shadow-md flex flex-col justify-between h-full"
              >
                <div className="flex-grow">
                  <img
                    src={`http://localhost:8000${auto.imagen}`}
                    alt={auto.nombre}
                    className="w-full h-60 object-contain rounded-lg mb-4"
                  />
                  <h3 className="text-lg font-bold mb-4">{auto.nombre}</h3>
                  <h3>
                    Marca:{" "}
                    <span className="text-gray-600">{auto.marca_id}</span>{" "}
                  </h3>
                  <h3>
                    Modelo:{" "}
                    <span className="text-gray-600">{auto.modelo_id}</span>{" "}
                  </h3>
                  <h3>
                    Estado:{" "}
                    <span className="text-gray-600">{auto.estado_id}</span>
                  </h3>
                  <h3>
                    Color:{" "}
                    <span className="text-gray-600">{auto.color_id}</span>
                  </h3>
                </div>

                <div className="flex justify-between mt-4">
                  <button
                    onClick={() => navigate(`/admin/editar-auto/${auto.id}`)}
                    className="bg-yellow-500 text-white px-4 py-2 rounded-lg hover:bg-yellow-600 transition hover:cursor-pointer"
                  >
                    Editar
                  </button>
                  <button
                    onClick={() => handleDelete(auto.id)}
                    className="bg-red-600 text-white px-4 py-2 rounded-lg hover:bg-red-700 transition hover:cursor-pointer"
                  >
                    Eliminar
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </>
  );
};

export default Admin;
