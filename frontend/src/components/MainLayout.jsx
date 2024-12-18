import Header from './Header'
import Footer from './Footer'
import { Outlet } from 'react-router-dom'

function MainLayout() {
  return (
    <div className="min-h-screen bg-gray-100">
        <Header />
          <Outlet />
        <Footer />
      </div>
  )
}

export default MainLayout