import { SidebarProvider } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/app-sidebar"
import { ChatbotDemo } from "@/components/ai-chat"

export default function DMAssistantPage() {
  return (
    <SidebarProvider>
      <div className="flex h-screen w-full overflow-hidden">
        <AppSidebar />
        <main className="flex min-w-0 flex-1 flex-col overflow-hidden">
          <ChatbotDemo />
        </main>
      </div>
    </SidebarProvider>
  )
}