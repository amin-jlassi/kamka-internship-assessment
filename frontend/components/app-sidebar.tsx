import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarHeader,
  SidebarGroupLabel
} from "@/components/ui/sidebar";
import { Button } from "./ui/button";


export function AppSidebar() {
  return (
    <Sidebar>
      <SidebarHeader />
      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupLabel className="text-md">
            Documents
          </SidebarGroupLabel>
        </SidebarGroup>
        <SidebarGroup />
      </SidebarContent>
      <SidebarFooter>
        <Button className="relative bottom-12">
          Upload resource
        </Button>
      </SidebarFooter>
    </Sidebar>
  )
}