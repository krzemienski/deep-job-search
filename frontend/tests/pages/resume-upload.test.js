import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import ResumeUpload from '../../pages/resume-upload'
import { useRouter } from 'next/router'

// Mock next/router
jest.mock('next/router', () => ({
  useRouter: jest.fn()
}))

// Mock fetch
global.fetch = jest.fn()

describe('ResumeUpload', () => {
  const mockRouter = {
    push: jest.fn()
  }

  beforeEach(() => {
    useRouter.mockReturnValue(mockRouter)
    global.fetch.mockClear()
    mockRouter.push.mockClear()
  })

  it('renders upload component', () => {
    render(<ResumeUpload />)
    expect(screen.getByText(/Upload Your Resume/i)).toBeInTheDocument()
    expect(screen.getByText(/We accept PDF, PNG, and JPEG formats/i)).toBeInTheDocument()
  })

  it('handles file upload', async () => {
    render(<ResumeUpload />)
    
    const file = new File(['dummy content'], 'test.pdf', { type: 'application/pdf' })
    const input = screen.getByLabelText(/Upload a file/i)
    
    global.fetch.mockImplementationOnce(() =>
      Promise.resolve({
        ok: true,
        json: () => Promise.resolve({
          message: 'Resume processed successfully',
          summary: { skills: ['JavaScript'] }
        })
      })
    )

    fireEvent.change(input, { target: { files: [file] } })
    
    const submitButton = screen.getByRole('button', { name: /Continue/i })
    fireEvent.click(submitButton)

    await waitFor(() => {
      expect(global.fetch).toHaveBeenCalledTimes(1)
      expect(mockRouter.push).toHaveBeenCalledWith('/preferences')
    })
  })

  it('shows error for invalid file type', () => {
    render(<ResumeUpload />)
    
    const file = new File(['dummy content'], 'test.txt', { type: 'text/plain' })
    const input = screen.getByLabelText(/Upload a file/i)
    
    fireEvent.change(input, { target: { files: [file] } })
    
    expect(screen.getByText(/Please upload a PDF or image file/i)).toBeInTheDocument()
  })

  it('handles upload error', async () => {
    render(<ResumeUpload />)
    
    const file = new File(['dummy content'], 'test.pdf', { type: 'application/pdf' })
    const input = screen.getByLabelText(/Upload a file/i)
    
    global.fetch.mockImplementationOnce(() =>
      Promise.resolve({
        ok: false,
        status: 500
      })
    )

    fireEvent.change(input, { target: { files: [file] } })
    
    const submitButton = screen.getByRole('button', { name: /Continue/i })
    fireEvent.click(submitButton)

    await waitFor(() => {
      expect(screen.getByText(/Failed to upload resume/i)).toBeInTheDocument()
    })
  })
})
