export interface ApiResponse {
  // Define your response type
  message: string;
  data: string;
}

export interface ApiError {
  message: string;
  status: number;
}
