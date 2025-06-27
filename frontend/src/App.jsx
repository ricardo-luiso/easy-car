import { BrowserRouter, Routes, Route } from "react-router-dom";
import InicioSesion from "./pages/InicioSesion";
import Admin from "./admin/Admin";
import Dashboard from "./pages/Dashboard";
import CrearUsuario from "./pages/CrearUsuario";
import CrearAuto from "./admin/CrearAuto";
import EditarAuto from "./admin/EditarAuto";
import RutaProtegida from "./RutasProtegida";
import PerfilAuto from "./components/Cars/PerfilAuto";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Rutas públicas */}
        <Route path="/" element={<Dashboard />} />
        <Route path="/crear-usuario" element={<CrearUsuario />} />
        <Route path="/login" element={<InicioSesion />} />
        <Route path="/perfil-auto/:id" element={<PerfilAuto />} />

        {/* Rutas protegidas */}
        <Route element={<RutaProtegida />}>
          <Route path="/admin" element={<Admin />} />
          <Route path="/admin/crear-auto" element={<CrearAuto />} />
          <Route path="/admin/editar-auto/:id" element={<EditarAuto />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
