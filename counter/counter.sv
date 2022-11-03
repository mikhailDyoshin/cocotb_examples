`timescale 1us/1us

module counter (
  input logic clk, reset,
  output logic [7:0] res
);

always @(posedge clk) begin
    if (reset)
        res <= 8'b0;
    else
        res <= res + 1'b1;
end

endmodule
