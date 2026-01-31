import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import App from './App';
import { vi } from 'vitest';

// Mock fetch globally
beforeEach(() => {
  global.fetch = vi.fn(() =>
    Promise.resolve({
      ok: true,
      json: () =>
        Promise.resolve({
          team_size: 5,
          issues: 3,
          predicted_duration: 120,
          predicted_cost: 50000,
          delay_risk: false,
        }),
    })
  );
});

afterEach(() => {
  vi.resetAllMocks();
});

test('renders prediction form', () => {
  render(<App />);
  expect(screen.getByLabelText(/Team Size/i)).toBeInTheDocument();
  expect(screen.getByLabelText(/Issues/i)).toBeInTheDocument();
});

test('predict button exists', () => {
  render(<App />);
  expect(screen.getByRole('button', { name: /Predict/i })).toBeInTheDocument();
});

test('fetches prediction from Spring backend and displays result', async () => {
  render(<App />);

  // Fill form inputs
  fireEvent.change(screen.getByLabelText(/Team Size/i), { target: { value: '5' } });
  fireEvent.change(screen.getByLabelText(/Issues/i), { target: { value: '3' } });

  // Click predict button
  fireEvent.click(screen.getByRole('button', { name: /Predict/i }));

  // Wait for fetch to be called
  await waitFor(() => {
    expect(global.fetch).toHaveBeenCalledTimes(1);
  });

  // Check displayed results
  expect(await screen.findByText(/Duration:/i)).toHaveTextContent('120');
  expect(await screen.findByText(/Cost:/i)).toHaveTextContent('50000');
  expect(await screen.findByText(/Delay Risk:/i)).toHaveTextContent('No');
});

test('handles API failure gracefully', async () => {
  global.fetch = vi.fn(() =>
    Promise.resolve({
      ok: false,
      status: 500,
    })
    
  );

  render(<App />);

  fireEvent.change(screen.getByLabelText(/Team Size/i), {
    target: { value: '5' },
  });

  fireEvent.change(screen.getByLabelText(/Issues/i), {
    target: { value: '3' },
  });

  fireEvent.click(screen.getByRole('button', { name: /Predict/i }));

  await waitFor(() => {
    expect(global.fetch).toHaveBeenCalled();
  });

  expect(await screen.findByText(/error/i)).toBeInTheDocument();
});
