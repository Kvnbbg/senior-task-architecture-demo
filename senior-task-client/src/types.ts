export type Priority = "low" | "medium" | "high" | "critical";
export type TaskStatus = "todo" | "in_progress" | "done" | "cancelled";

export interface TaskCreate {
  title: string;
  description?: string | null;
  priority: Priority;
  due_date?: string | null; // ISO date
}

export interface Task extends TaskCreate {
  id: number;
  status: TaskStatus;
  created_at: string; // ISO datetime
  updated_at: string;
}

export interface TaskUpdate {
  title?: string;
  description?: string | null;
  priority?: Priority;
  status?: TaskStatus;
  due_date?: string | null;
}
