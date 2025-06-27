import Navbar from "../components/Navbar/Navbar";
import { useParams, useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";

const EditarAuto = () => {
  const [formData, setFormData] = useState({
    id: "",
    nombre: "",
    marca_id: "",
    modelo_id: "",
    combustible_id: "",
    estado_id: "",
    color_id: "",
    imagen: "", // URL string o File
  });

  const navigate = useNavigate();
  const { id } = useParams();
  const [imagenActual, setImagenActual] = useState("");

  useEffect(() => {
    const getAuto = async () => {
      const token = localStorage.getItem("token");
      const response = await fetch(`http://localhost:8000/autos/${id}`, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      const data = await response.json();

      setFormData({
        id: data.id,
        nombre: data.nombre,
        marca_id: data.marca_id,
        modelo_id: data.modelo_id,
        combustible_id: data.combustible_id,
        estado_id: data.estado_id,
        color_id: data.color_id,
        imagen: "", // no incluimos la imagen como File, solo la URL por separado
      });
      setImagenActual(data.imagen);
    };

    getAuto();
  }, [id]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const token = localStorage.getItem("token");

    const formDataToSend = new FormData();
    formDataToSend.append("nombre", formData.nombre);
    formDataToSend.append("marca_id", formData.marca_id);
    formDataToSend.append("modelo_id", formData.modelo_id);
    formDataToSend.append("combustible_id", formData.combustible_id);
    formDataToSend.append("estado_id", formData.estado_id);
    formDataToSend.append("color_id", formData.color_id);

    // Si el usuario seleccionó una nueva imagen
    if (formData.imagen) {
      formDataToSend.append("imagen", formData.imagen);
    }

    const request = await fetch(`http://localhost:8000/autos/${id}`, {
      method: "PUT",
      headers: {
        Authorization: `Bearer ${token}`,
      },
      body: formDataToSend,
    });

    const response = await request.json();

    if (response.msg == "ok") {
      alert("Auto editado exitosamente");
      navigate("/admin");
    } else {
      alert("Error al editar el auto: " + response.message);
    }
  };

  return (
    <>
      <Navbar />
      <div className="min-h-screen bg-gray-100 p-6">
        <h1 className="text-3xl font-bold mb-6 text-center">Editar Auto</h1>
        <form
          onSubmit={handleSubmit}
          className="max-w-2xl mx-auto bg-white p-6 rounded-lg shadow-md space-y-4"
        >
          <div>
            <label htmlFor="nombre">Nombre:</label>
            <input
              value={formData.nombre}
              onChange={(e) =>
                setFormData({ ...formData, nombre: e.target.value })
              }
              type="text"
              id="nombre"
              name="nombre"
              className="border border-gray-300 rounded-lg p-2 w-full"
              required
            />
          </div>

          {["marca", "modelo", "combustible", "estado", "color"].map(
            (campo) => (
              <div key={campo}>
                <label htmlFor={campo}>
                  {campo.charAt(0).toUpperCase() + campo.slice(1)}:
                </label>
                <input
                  value={formData[`${campo}_id`]}
                  onChange={(e) =>
                    setFormData({
                      ...formData,
                      [`${campo}_id`]: e.target.value,
                    })
                  }
                  type="text"
                  id={campo}
                  name={campo}
                  className="border border-gray-300 rounded-lg p-2 w-full"
                  required
                />
              </div>
            )
          )}

          {/* Imagen actual */}
          <div className="mb-4">
            {/* Imagen actual o nueva preview */}
            {formData.imagen && typeof formData.imagen === "object" ? (
              <img
                src={URL.createObjectURL(formData.imagen)}
                alt="Preview de la nueva imagen"
                className="w-full h-60 object-contain rounded-lg mb-4"
              />
            ) : (
              imagenActual && (
                <img
                  alt="Imagen actual del auto"
                  className="w-full h-60 object-contain rounded-lg mb-4"
                  src={`http://localhost:8000${imagenActual}`}
                />
              )
            )}

            <label
              htmlFor="imagen"
              className="block text-sm font-medium text-gray-700 mb-1"
            >
              Nueva Imagen (opcional):
            </label>

            <input
              accept="image/*"
              onChange={(e) =>
                setFormData({ ...formData, imagen: e.target.files[0] })
              }
              type="file"
              id="imagen"
              name="imagen"
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
            Editar Auto
          </button>
        </form>
      </div>
    </>
  );
};

export default EditarAuto;
