import { render, screen } from '@testing-library/react';
import App from './App';

test('renders welcome message', () => {
  render(<App />);
  const welcomeMessage = screen.getByText(/Welcome to Octofit Tracker/i);
  expect(welcomeMessage).toBeInTheDocument();
});
