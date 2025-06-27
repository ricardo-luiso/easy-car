import Navbar from "../components/Navbar/Navbar";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const CrearAuto = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    nombre: "",
    marca_id: "",
    modelo_id: "",
    combustible_id: "",
    estado_id: "",
    color_id: "",
    imagen: "",
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    const token = localStorage.getItem("token");
    const formDataToSend = new FormData();
    for (const key in formData) {
      formDataToSend.append(key, formData[key]);
    }

    const request = await fetch("http://localhost:8000/autos/", {
      method: "POST",
      body: formDataToSend,
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    const response = await request.json();

    if (response.message == "ok") {
      alert("Auto creado exitosamente");
      navigate("/admin");
    } else {
      alert("Error al crear el auto: " + response.message);
    }
  };

  return (
    <>
      <Navbar />
      <div className="min-h-screen bg-gray-100 p-6">
        <h1 className="text-3xl font-bold mb-6 text-center">Crear Auto</h1>
        <form
          onSubmit={handleSubmit}
          className="max-w-2xl mx-auto bg-white p-6 rounded-lg shadow-md space-y-4"
        >
          <div>
            <label htmlFor="nombre">Nombre:</label>
            <input
              onChange={(e) =>
                setFormData({ ...formData, nombre: e.target.value })
              }
              type="text"
              id="nombre"
              name="nombre"
              autoComplete="off"
              required
              className="border border-gray-300 rounded-lg p-2 w-full"
            />
          </div>
          <div>
            <label htmlFor="marca">Marca:</label>
            <input
              onChange={(e) =>
                setFormData({ ...formData, marca_id: e.target.value })
              }
              type="text"
              id="marca"
              name="marca"
              required
              className="border border-gray-300 rounded-lg p-2 w-full"
            />
          </div>
          <div>
            <label htmlFor="modelo">Modelo:</label>
            <input
              onChange={(e) =>
                setFormData({ ...formData, modelo_id: e.target.value })
              }
              type="text"
              id="modelo"
              name="modelo"
              required
              className="border border-gray-300 rounded-lg p-2 w-full"
            />
          </div>

          <div>
            <label htmlFor="combustible">Combustible:</label>
            <input
              onChange={(e) =>
                setFormData({ ...formData, combustible_id: e.target.value })
              }
              type="text"
              id="combustible"
              name="combustible"
              required
              className="border border-gray-300 rounded-lg p-2 w-full"
            />
          </div>

          <div>
            <label htmlFor="estado">Estado:</label>
            <input
              onChange={(e) =>
                setFormData({ ...formData, estado_id: e.target.value })
              }
              type="text"
              id="estado"
              name="estado"
              required
              className="border border-gray-300 rounded-lg p-2 w-full"
            />
          </div>

          <div>
            <label htmlFor="color">Color:</label>
            <input
              onChange={(e) =>
                setFormData({ ...formData, color_id: e.target.value })
              }
              type="text"
              id="color"
              name="color"
              required
              className="border border-gray-300 rounded-lg p-2 w-full"
            />
          </div>

          <div className="mb-4">
            <label
              htmlFor="imagen"
              className="block text-sm font-medium text-gray-700 mb-1"
            >
              Imagen:
            </label>
            <input
              onChange={(e) =>
                setFormData({ ...formData, imagen: e.target.files[0] })
              }
              type="file"
              id="imagen"
              name="imagen"
              required
              className="block w-full text-sm text-gray-500
               file:mr-4 file:py-2 file:px-4
               file:rounded-lg file:border-0
               file:text-sm file:font-semibold
               file:bg-blue-50 file:text-blue-700
               hover:file:bg-blue-100 hover:cursor-pointer"
            />
          </div>

          <button
            type="submit"
            className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition hover:cursor-pointer w-full"
          >
            Crear Auto
          </button>
        </form>
      </div>
    </>
  );
};

export default CrearAuto;
