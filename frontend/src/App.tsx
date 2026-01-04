import { BrowserRouter, Routes, Route } from 'react-router-dom'
import EventsList from './events/pages/EventsList'
import CreateEvent from './events/pages/CreateEvent'
import PreEvent from './events/pages/PreEvent'
import LiveEvent from './events/pages/LiveEvent'
import PostEvent from './events/pages/PostEvent'

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/events" element={<EventsList />} />
        <Route path="/events/create" element={<CreateEvent />} />
        <Route path="/events/:id/pre-event" element={<PreEvent />} />
        <Route path="/events/:id/live" element={<LiveEvent />} />
        <Route path="/events/:id/post-event" element={<PostEvent />} />
      </Routes>
    </BrowserRouter>
  )
}
