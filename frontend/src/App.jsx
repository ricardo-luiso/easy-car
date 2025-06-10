import CarList from "./components/CarList";
import Navbar from "./components/Navbar";
import SideBar from "./components/SideBar";

function App() {
  return (
    <>
      <Navbar />
      <img
        className="h-[70vh] w-full object-cover"
        src="carusel-1.png"
        alt=""
      />

      <section className="mx-10 grid grid-cols-5 gap-4 p-4">
        <SideBar />
        <CarList />
      </section>
    </>
  );
}

export default App;
